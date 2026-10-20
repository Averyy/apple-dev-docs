# init(address:mask:)

**Framework**: AVRouting  
**Kind**: init  
**Role**: Initializer

Creates an IP fragment.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- visionOS 1.0+

## Declaration

```swift
init(address: Data, mask: Data)
```

```objc
- (instancetype) initWithAddress:(NSData *) address mask:(NSData *) mask;
```

## Parameters

- `address`: The IP address.
- `mask`: The address mask.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avrouting/avcustomroutingpartialip/init(address:mask:))*