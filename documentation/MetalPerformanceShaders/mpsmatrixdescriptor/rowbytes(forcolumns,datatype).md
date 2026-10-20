# rowBytes(forColumns:dataType:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Type Method

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func rowBytes(forColumns columns: Int, dataType: MPSDataType) -> Int
```

```objc
+ (size_t) rowBytesForColumns:(NSUInteger) columns dataType:(MPSDataType) dataType;
```

## See Also

### Methods
- [convenience init(dimensions: Int, columns: Int, rowBytes: Int, dataType: MPSDataType)](./init%28dimensions,columns,rowbytes,datatype%29.md)
  Creates a matrix descriptor with the specified dimensions and data type.
- [class func rowBytes(fromColumns: Int, dataType: MPSDataType) -> Int](./rowbytes%28fromcolumns,datatype%29.md)
  Determines the recommended matrix row stride, in bytes, for a given number of columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsmatrixdescriptor/rowbytes(forcolumns:datatype:))*