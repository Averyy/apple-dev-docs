# title

**Framework**: SwiftUI  
**Kind**: property

The hosting view’s associated window will have its title and subtitle populated with the values provided to the `navigationTitle(_:)` and `navigationSubtitle(_:)` modifiers, respectively.

**Availability**:
- macOS 14.0+

## Declaration

```swift
static let title: NSHostingSceneBridgingOptions
```

#### Discussion

Title bars populated in this manner overwrite any values set using AppKit.

## See Also

- [static let all: NSHostingSceneBridgingOptions](nshostingscenebridgingoptions/all.md)
  The hosting view’s associated window will have both its title bars and toolbars populated with values from their respective modifiers.
- [static let toolbars: NSHostingSceneBridgingOptions](nshostingscenebridgingoptions/toolbars.md)
  The hosting view’s associated window will have its toolbar populated with any items provided to the `toolbar(content:)` modifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingscenebridgingoptions/title)*