# init(full:supporting:systemImageName:)

**Framework**: App Intents  
**Kind**: init

The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst ?+
- macOS 14.2+
- tvOS 17.2+
- visionOS ?+
- watchOS 10.2+

## Declaration

```swift
init(full: LocalizedStringResource, supporting: LocalizedStringResource, systemImageName: String)
```

#### Discussion

Parameters:

- full: a standalone message that fully describes the output
- supporting: a message that may be used in conjunction with visual output
- systemImageName: an SF Symbol that may be be used to represent the result

## See Also

- [init(LocalizedStringResource)](intentdialog/init(_:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource)](intentdialog/init(full:supporting:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, systemImageName: String)](intentdialog/init(full:systemimagename:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdialog/init(full:supporting:systemimagename:))*