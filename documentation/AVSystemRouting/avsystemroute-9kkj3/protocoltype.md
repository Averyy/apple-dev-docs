# protocolType

**Framework**: AVSystemRouting  
**Kind**: property  
**Role**: Instance Property

The communication protocol the active route uses.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
@property (copy, readonly) UTType * protocolType;
```

#### Discussion

The protocol’s `identifier` property enables your app to adapt its behavior based on the selected protocol. The protocol’s display name and icon can also be obtained from the `UTType`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroute-9kkj3/protocoltype)*