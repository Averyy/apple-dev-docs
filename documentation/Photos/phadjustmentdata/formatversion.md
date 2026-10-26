# formatVersion

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A version number for the adjustment data format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var formatVersion: String { get }
```

```objc
@property (copy, readonly) NSString * formatVersion;
```

#### Discussion

Set this identifier when creating an adjustment object with the [`init(formatIdentifier:formatVersion:data:)`](./init%28formatidentifier,formatversion,data%29.md) method.

Read this property, and the [`formatIdentifier`](./formatidentifier.md) property, to determine whether the adjustment data saved with an asset was created by your app or is otherwise compatible with your app.

For example, in the first version of your app, you might save adjustment data using the identifier `com.example.myApp` and version `1.0`. If a later version of your app adds incompatible information to the adjustment data, you can use the same identifier and increase the version number to `2.0`.

## See Also

### Identifying the Format of an Adjustment’s Data
- [var formatIdentifier: String](./formatidentifier.md)
  A string uniquely identifying the format of the adjustment data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phadjustmentdata/formatversion)*