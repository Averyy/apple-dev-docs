# init(full:supporting:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
init(full: LocalizedStringResource, supporting: LocalizedStringResource)
```

#### Discussion

Parameters:

- full: a standalone message that fully describes the output
- supporting: a message that may be used in conjunction with visual output

## See Also

### Creating a dialog
- [init(LocalizedStringResource)](./init%28_%29.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, systemImageName: String)](./init%28full,systemimagename%29.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource, systemImageName: String)](./init%28full,supporting,systemimagename%29.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdialog/init(full:supporting:))*