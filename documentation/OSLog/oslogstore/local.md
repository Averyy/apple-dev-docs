# local()

**Framework**: OSLog  
**Kind**: method

Creates a log store representing the Mac’s local store.

**Availability**:
- macOS 10.15+

## Declaration

```swift
class func local() throws -> Self
```

#### Discussion

Gaining access to the local unified logging system requires permission from the system. The caller must be run by an admin account and have the `com.apple.logging.local-store` entitlement.

## See Also

- [convenience init(url: URL) throws](oslogstore/init(url:).md)
  Creates a log store based on a log archive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/oslog/oslogstore/local())*