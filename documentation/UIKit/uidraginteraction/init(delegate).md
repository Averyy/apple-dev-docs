# init(delegate:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes a drag interaction object with a custom delegate object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(delegate: any UIDragInteractionDelegate)
```

```objc
- (instancetype) initWithDelegate:(id<UIDragInteractionDelegate>) delegate;
```

#### Return Value

A drag interaction that has a delegate.

## Parameters

- `delegate`: The object that configures and controls a drag interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteraction/init(delegate:))*