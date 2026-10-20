# dismissPopover(_:)

**Framework**: Shared with You  
**Kind**: method  
**Role**: Instance Method

Dismisses the popover.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func dismissPopover(_ completion: (() -> Void)? = nil)
```

```swift
func dismissPopover() async
```

```objc
- (void) dismissPopover:(void (^)()) completion;
```

## Parameters

- `completion`: The system calls this handler after the system finishes dismissing the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swcollaborationview/dismisspopover(_:))*