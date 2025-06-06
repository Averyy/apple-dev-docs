# contactAccessPicker(isPresented:completionHandler:)

**Framework**: SwiftUI  
**Kind**: method

Modally present UI which allows the user to select which contacts your app has access to.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
@MainActor
@preconcurrency func contactAccessPicker(isPresented: Binding<Bool>, completionHandler: @escaping ([String]) -> () = {_ in }) -> some View
```

#### Discussion

This API should only be used when your app has “Limited” authorization.  See `CNAuthorizationStatus` and `CNContactStore/authorizationStatus(for:)`.  The completion handler will be invoked with an empty result if your app doesn’t have the correct authorization status.

Your completion handler will receive an array of contact identifiers that were newly granted to your app.  Contacts which your app lost access to are not listed.  The newly-available contacts can be accessed using `CNContactStore`.

Parameters:

- isPresented: The binding to whether the contact picker should be shown.
- completionHandler: A function to invoke when the management UI is dismissed.  Receives an array containing contact identifiers of newly-available contacts.

## See Also

- [func contactAccessButtonCaption(ContactAccessButton.Caption) -> some View](view/contactaccessbuttoncaption(_:).md)
- [func contactAccessButtonStyle(ContactAccessButton.Style) -> some View](view/contactaccessbuttonstyle(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/contactaccesspicker(ispresented:completionhandler:))*