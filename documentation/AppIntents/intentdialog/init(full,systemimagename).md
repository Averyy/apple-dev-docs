# init(full:systemImageName:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- macOS 14.2+
- tvOS 17.2+
- visionOS
- watchOS 10.2+

## Declaration

```swift
init(full: LocalizedStringResource, systemImageName: String)
```

## Discussion

Parameters:

- full: a standalone message that fully describes the output
- systemImageName: an SF Symbol that may be be used to represent the result

## See Also

### Creating a dialog
- [init(LocalizedStringResource)](./init%28_%29.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource)](./init%28full,supporting%29.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource, systemImageName: String)](./init%28full,supporting,systemimagename%29.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdialog/init(full:systemimagename:))*