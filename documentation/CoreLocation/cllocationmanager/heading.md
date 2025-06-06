# heading

**Framework**: Core Location  
**Kind**: property

The most recently reported heading.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var heading: CLHeading? { get }
```

#### Discussion

The value of this property is `nil` if heading updates have never been initiated.

## See Also

- [var location: CLLocation?](cllocationmanager/location.md)
  The most recently retrieved user location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationmanager/heading)*