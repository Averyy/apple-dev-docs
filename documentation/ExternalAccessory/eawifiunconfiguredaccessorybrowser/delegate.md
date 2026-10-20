# delegate

**Framework**: External Accessory  
**Kind**: property  
**Role**: Instance Property

The object that acts as the delegate of the browser and receives browser events.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any EAWiFiUnconfiguredAccessoryBrowserDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<EAWiFiUnconfiguredAccessoryBrowserDelegate> delegate;
```

## See Also

### Managing Browser Interactions
- [protocol EAWiFiUnconfiguredAccessoryBrowserDelegate](../eawifiunconfiguredaccessorybrowserdelegate.md)
  A protocol you use to manage the search and configuration processes for an unconfigured accessory browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalaccessory/eawifiunconfiguredaccessorybrowser/delegate)*