# init(domain:)

**Framework**: ManagedSettings  
**Kind**: init

Creates an object that represents the specified web domain.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
init(domain: String)
```

#### Discussion

Provide a high-level domain, such as `example.com`. To protect a family’s privacy, use [`init(token:)`](webdomain/init(token:).md) instead.

## Parameters

- `domain`: A website to allow or block.

## See Also

- [init(token: WebDomainToken)](webdomain/init(token:).md)
  Creates an object that represents the provided domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webdomain/init(domain:))*