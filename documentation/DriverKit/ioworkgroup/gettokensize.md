# GetTokenSize

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
size_t GetTokenSize();
```

#### Return Value

Workgroup token size

#### Discussion

Get the size of the workgroup token.

Join() and Leave() require the caller to pass a token. This token should be allocated by the caller, and freed when no longer needed. Use this method to determine how much memory to allocate for the token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioworkgroup/gettokensize)*