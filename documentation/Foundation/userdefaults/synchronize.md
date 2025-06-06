# synchronize()

**Framework**: Foundation  
**Kind**: method

Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func synchronize() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the data was saved successfully to disk, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func removePersistentDomain(forName: String)](userdefaults/removepersistentdomain(forname:).md)
  Removes the contents of the specified persistent domain from the user’s defaults.
- [func persistentDomain(forName: String) -> [String : Any]?](userdefaults/persistentdomain(forname:).md)
  Returns a dictionary representation of the defaults for the specified domain.
- [func setPersistentDomain([String : Any], forName: String)](userdefaults/setpersistentdomain(_:forname:).md)
  Sets a dictionary for the specified persistent domain.
- [convenience init?(user: String)](userdefaults/init(user:).md)
  Creates a user defaults object initialized with the defaults for the specified user account.
- [class func resetStandardUserDefaults()](userdefaults/resetstandarduserdefaults.md)
  This method has no effect and shouldn’t be used.
- [Language-Dependent Information Constants](language-dependent-information-constants.md)
  These constants are deprecated and shouldn’t be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/synchronize())*