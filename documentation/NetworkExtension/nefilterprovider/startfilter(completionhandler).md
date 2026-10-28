# startFilter(completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Start the filter.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func startFilter(completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func startFilter() async throws
```

```objc
- (void) startFilterWithCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

This method is called by the system to start the filter.

`NEFilterProvider` subclasses must override this method.

When this method is called, the Filter Provider should perform any steps necessary to initialize the filter and then execute the `completionHandler` block.

## Parameters

- `completionHandler`: A block that must be executed when the filter is running and is ready to filter network content.

## See Also

### Managing the filter life cycle
- [func stopFilter(with: NEProviderStopReason, completionHandler: () -> Void)](./stopfilter%28with,completionhandler%29.md)
  Stop the filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefilterprovider/startfilter(completionhandler:))*