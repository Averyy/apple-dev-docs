# statistics

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A dictionary containing various statistics for the receiver.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (copy, readonly) NSDictionary<NSString *,NSNumber *> * statistics;
```

#### Discussion

An `NSDictionary` object containing various statistics for the receiver, such as the number of vended objects, the number of requests and replies, and so on.

The statistics dictionary should be used only for debugging purposes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/statistics-c.property)*