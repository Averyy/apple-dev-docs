# mapTemplate(_:didFailToShareDestinationFor:error:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Called when a vehicle failed to handle a shared trip’s destination

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
optional func mapTemplate(_ mapTemplate: CPMapTemplate, didFailToShareDestinationFor trip: CPTrip, error: any Error)
```

```objc
- (void) mapTemplate:(CPMapTemplate *) mapTemplate didFailToShareDestinationForTrip:(CPTrip *) trip error:(NSError *) error;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmaptemplatedelegate/maptemplate(_:didfailtosharedestinationfor:error:))*