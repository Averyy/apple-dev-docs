# init(dictionary:)

**Framework**: Foundation  
**Kind**: init

Initializes a newly allocated dictionary and adds to it objects from another given dictionary.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@objc
(__swiftInitWithDictionary_NSDictionary:) dynamic convenience init(dictionary otherDictionary: NSDictionary)
```

#### Return Value

An initialized dictionary–which might be different than the original receiver–containing the keys and values found in `otherDictionary`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdictionary/init(dictionary:)-4gc13)*