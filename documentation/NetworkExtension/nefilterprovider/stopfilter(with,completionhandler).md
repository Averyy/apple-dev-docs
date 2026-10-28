# stopFilter(with:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Stop the filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func stopFilter(with reason: NEProviderStopReason, completionHandler: @escaping @Sendable () -> Void)
```

```swift
func stopFilter(with reason: NEProviderStopReason) async
```

```objc
- (void) stopFilterWithReason:(NEProviderStopReason) reason completionHandler:(void (^)()) completionHandler;
```

## Discussion

This method is called by the system to stop the filter.

`NEFilterProvider` subclasses must override this method.

## Parameters

- `reason`: An `NEProviderStopReason` code indicating why the filter is being stopped. For a list of possible codes, see [`NEProvider`](../neprovider.md).
- `completionHandler`: A block that must be executed when the filter is fully stopped.

## See Also

### Managing the filter life cycle
- [func startFilter(completionHandler: ((any Error)?) -> Void)](./startfilter%28completionhandler%29.md)
  Start the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterprovider/stopfilter(with:completionhandler:))*