# dataSourceID

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The system-assigned identifier for the data source.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var dataSourceID: NSNumber { get }
```

```objc
@property (readonly) NSNumber * dataSourceID;
```

## Discussion

You can use the value of this property to assign a specific data source to some input or output within an audio session.

## See Also

### Identifying a data source
- [var dataSourceName: String](./datasourcename.md)
  A human-readable name for the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondatasourcedescription/datasourceid)*