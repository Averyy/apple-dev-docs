# toolbars

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Type Property

The hosting view’s associated window will have its toolbar populated with any items provided to the `toolbar(content:)` modifier.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static let toolbars: NSHostingSceneBridgingOptions
```

## Discussion

Toolbars populated in this manner overwrite any toolbar set on the window using AppKit.

## See Also

### Geting bridging options
- [static let all: NSHostingSceneBridgingOptions](./all.md)
  The hosting view’s associated window will have both its title bars and toolbars populated with values from their respective modifiers.
- [static let title: NSHostingSceneBridgingOptions](./title.md)
  The hosting view’s associated window will have its title and subtitle populated with the values provided to the `navigationTitle(_:)` and `navigationSubtitle(_:)` modifiers, respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingscenebridgingoptions/toolbars)*