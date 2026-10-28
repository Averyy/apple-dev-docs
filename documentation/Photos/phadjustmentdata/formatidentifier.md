# formatIdentifier

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A string uniquely identifying the format of the adjustment data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var formatIdentifier: String { get }
```

```objc
@property (copy, readonly) NSString * formatIdentifier;
```

## Discussion

Set this identifier when you create an adjustment object with the [`init(formatIdentifier:formatVersion:data:)`](./init%28formatidentifier,formatversion,data%29.md) method. For best results, identify your organization or product using a reverse-DNS-style name, such as `com.example.myApp`.

Read this property, and the [`formatVersion`](./formatversion.md) property, to determine whether the adjustment data saved with an asset was created by your app or is otherwise compatible with your app.

## See Also

### Identifying the Format of an Adjustment’s Data
- [var formatVersion: String](./formatversion.md)
  A version number for the adjustment data format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phadjustmentdata/formatidentifier)*