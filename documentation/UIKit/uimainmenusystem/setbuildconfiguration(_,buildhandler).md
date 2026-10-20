# setBuildConfiguration(_:buildHandler:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency func setBuildConfiguration(_ configuration: UIMainMenuSystem.Configuration, buildHandler: ((any UIMenuBuilder) -> Void)? = nil)
```

## See Also

### Configuring a main menu system
- [UIMainMenuSystem.Configuration](./configuration.md)
  A configuration for the main menu system. You can specify whether or not certain elements are present in the initial main menu, as well as a block to build the menu using a UIMenuBuilder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimainmenusystem/setbuildconfiguration(_:buildhandler:))*