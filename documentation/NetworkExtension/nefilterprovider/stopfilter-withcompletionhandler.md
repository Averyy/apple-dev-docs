# stopFilter(with:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Stop the filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func stopFilter(with reason: NEProviderStopReason) async
```

#### Discussion

This method is called by the system to stop the filter.

`NEFilterProvider` subclasses must override this method.

## Parameters

- `reason`: An   code indicating why the filter is being stopped. For a list of possible codes, see  .
- `completionHandler`: A block that must be executed when the filter is fully stopped.

## See Also

- [func startFilter(completionHandler: ((any Error)?) -> Void)](nefilterprovider/startfilter(completionhandler:).md)
  Start the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterprovider/stopfilter(with:completionhandler:))*