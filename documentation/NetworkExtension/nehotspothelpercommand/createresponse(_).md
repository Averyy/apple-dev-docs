# createResponse(_:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Create a response to the command.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func createResponse(_ result: NEHotspotHelperResult) -> NEHotspotHelperResponse
```

```objc
- (NEHotspotHelperResponse *) createResponse:(NEHotspotHelperResult) result;
```

## Return Value

A NEHotspostHelperResponse object.

## Parameters

- `result`: The result of handling the command.

## See Also

### Response creation
- [enum NEHotspotHelperResult](../nehotspothelperresult.md)
  The result of handling a hotspot command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/createresponse(_:))*