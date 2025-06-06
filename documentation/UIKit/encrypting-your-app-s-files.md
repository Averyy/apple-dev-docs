# Encrypting Your App’s Files

**Framework**: UIKit

Protect the user’s data in iOS by encrypting it on disk.

#### Overview

Data protection is an iOS feature that you use to secure your app’s files and prevent unauthorized access to them. Data protection is enabled automatically when the user sets an active passcode for the device. You read and write your files normally, but the system encrypts and decrypts your content behind the scenes. The encryption and decryption processes are automatic and hardware accelerated.

You specify the level of data protection that you want to apply to each of your files. There are four levels available, each of which determines when you may access the file. If you do not specify a protection level when creating a file, iOS applies the default protection level automatically.

-  The file is always accessible.
-  (Default) The file is inaccessible until the first time the user unlocks the device. After the first unlocking of the device, the file remains accessible until the device shuts down or reboots.
-  You can open existing files only when the device is unlocked. If you have a file already open, you may continue to access that file even after the user locks the device. You can also create new files and access them while the device is locked or unlocked.
-  The file is accessible only when the device is unlocked.

To create and encrypt a new file in one step, construct a data object with the file’s contents and call the [`write(to:options:)`](https://developer.apple.com/documentation/foundation/data/1779858-write) method. When calling the method, specify the data protection option that you want applied to the file. The following code shows an example of how to write out the contents of a [`Data`](https://developer.apple.com/documentation/Foundation/Data) instance to a file and encrypt it using the complete protection level.

```swift
do {
   try data.write(to: fileURL, options: .completeFileProtection)
}
catch {
   // Handle errors.
}
```

To change the data protection level of an existing file, use the [`setResourceValue(_:forKey:)`](https://developer.apple.com/documentation/foundation/nsurl/1413819-setresourcevalue) method of [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL). When calling this method, assign the new data protection option to the [`fileProtectionKey`](https://developer.apple.com/documentation/foundation/urlresourcekey/1616246-fileprotectionkey) resource key. The following code shows an example that adds this key to an existing file.

```swift
do {
   try (fileURL as NSURL).setResourceValue( 
                  URLFileProtection.complete,
                  forKey: .fileProtectionKey)
}
catch {
   // Handle errors.
}
```

##### Manage Your Access to Encrypted Files

Depending on a file’s protection level, attempts to read or write its contents could fail when the user subsequently locks the device. To ensure that your app is able to access files, do the following:

- Choose the right data protection level for your needs.
- Use the app delegate’s [`applicationProtectedDataWillBecomeUnavailable(_:)`](uiapplicationdelegate/applicationprotecteddatawillbecomeunavailable(_:).md) and [`applicationProtectedDataDidBecomeAvailable(_:)`](uiapplicationdelegate/applicationprotecteddatadidbecomeavailable(_:).md) methods to close and reopen files with the [`completeFileProtection`](https://developer.apple.com/documentation/foundation/nsdata/writingoptions/1617198-completefileprotection) level.

Assign the complete protection level to files that your app accesses only when it is in the foreground. If your app supports background capabilities, such as handling location updates, assign a different protection level for files that you might access while in the background. For example, a fitness app might use the complete unless open protection level on a file that it uses to log location events in the background.

Files containing personal information about the user, or files created directly by the user, always warrant the strongest level of protection. Assign the complete protection level to user data files and manage access to those files using the app delegate methods. The app delegate methods give you time to close the files before they become inaccessible to your app.

## See Also

- [Requesting access to protected resources](requesting-access-to-protected-resources.md)
  Provide a purpose string that explains to a person why you need access to protected resources on their device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/encrypting-your-app-s-files)*