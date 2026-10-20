# focusItemContainer

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The container for the child focus items in this focus environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var focusItemContainer: (any UIFocusItemContainer)? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) id<UIFocusItemContainer> focusItemContainer;
```

#### Discussion

The value of this property is `nil` when no container exists.

## See Also

### Checking the ancestry of the environment
- [var parentFocusEnvironment: (any UIFocusEnvironment)?](./parentfocusenvironment.md)
  The parent focus environment for this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/focusitemcontainer)*