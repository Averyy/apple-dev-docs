# keyboardType(_:)

**Framework**: MusicKit  
**Kind**: method

Sets the keyboard type for this view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func keyboardType(_ type: UIKeyboardType) -> some View
```

#### Discussion

Use `keyboardType(_:)` to specify the keyboard type to use for text entry. A number of different keyboard types are available to meet specialized input needs, such as entering email addresses or phone numbers.

The example below presents a `TextField` to input an email address. Setting the text field’s keyboard type to `.emailAddress` ensures the user can only enter correctly formatted email addresses.

```swift
TextField("someone@example.com", text: $emailAddress)
    .keyboardType(.emailAddress)
```

There are several different kinds of specialized keyboard types available though the [`UIKeyboardType`](https://developer.apple.com/documentation/UIKit/UIKeyboardType) enumeration. To specify the default system keyboard type, use `.default`.

## Parameters

- `type`: One of the keyboard types defined in the    enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/keyboardtype(_:))*