# encode(contentsOf:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Encodes the elements of the given sequence.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func encode<T>(contentsOf sequence: T) throws where T : Sequence, T.Element == UInt
```

#### Discussion

> **Throws**: An error if any of the contained values throws an error.

## Parameters

- `sequence`: The sequences whose contents to encode.

## Default Implementations

### UnkeyedEncodingContainer Implementations
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-1k4wu.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-28q9o.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-2rt93.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-2yymi.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-4lzqs.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-59l2f.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-5zeys.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-6e9jx.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-7485u.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-74qqt.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-7pqnf.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-97v19.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-9cu3t.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-9dfsi.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-9lwpz.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-zmlx.md)
- [func encode<T>(contentsOf: T) throws](./encode%28contentsof%29-zo1s.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(contentsof:)-7m806)*