# setBuildConfiguration(_:buildHandler:)

**Framework**: UIKit  
**Kind**: method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func setBuildConfiguration(_ configuration: UIMainMenuSystem.Configuration, buildHandler: ((any UIMenuBuilder) -> Void)? = nil)
```

## See Also

- [UIMainMenuSystem.Configuration](uimainmenusystem/configuration.md)
  A configuration for the main menu system. You can specify whether or not certain elements are present in the initial main menu, as well as a block to build the menu using a UIMenuBuilder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimainmenusystem/setbuildconfiguration(_:buildhandler:))*