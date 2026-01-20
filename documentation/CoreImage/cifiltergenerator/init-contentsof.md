# init(contentsOf:)

**Framework**: Core Image  
**Kind**: init

Initializes a filter generator object with the contents of a filter generator file.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init?(contentsOf aURL: URL)
```

#### Return Value

The initialized [`CIFilterGenerator`](cifiltergenerator.md) object. Returns `nil` if the file can’t be read.

## Parameters

- `aURL`: The location of a filter generator file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifiltergenerator/init(contentsof:))*