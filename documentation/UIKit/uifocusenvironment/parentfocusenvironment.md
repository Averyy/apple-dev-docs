# parentFocusEnvironment

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The parent focus environment for this environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
weak var parentFocusEnvironment: (any UIFocusEnvironment)? { get }
```

```objc
@property (nonatomic, weak, readonly, nullable) id<UIFocusEnvironment> parentFocusEnvironment;
```

## Discussion

The value of this property is `nil` when no parent container exists.

## See Also

### Checking the ancestry of the environment
- [var focusItemContainer: (any UIFocusItemContainer)?](./focusitemcontainer.md)
  The container for the child focus items in this focus environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusenvironment/parentfocusenvironment)*