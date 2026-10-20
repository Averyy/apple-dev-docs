# init(_:)

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
init(_ string: LocalizedStringResource)
```

#### Discussion

Parameters:

- string: a standalone message that fully describes the output

## See Also

### Creating a dialog
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource)](./init%28full,supporting%29.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, systemImageName: String)](./init%28full,systemimagename%29.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource, systemImageName: String)](./init%28full,supporting,systemimagename%29.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdialog/init(_:))*