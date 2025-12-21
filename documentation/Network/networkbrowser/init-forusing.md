# init(for:using:)

**Framework**: Network  
**Kind**: init

Create a browser that will browse for the service specified by a BrowserProvider, with parameters.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(for provider: Provider, using parameters: NWParameters? = nil)
```

## Parameters

- `provider`: A BrowserProvider that describes the kind of   service to browse for, the browse descriptor,   and parameter configuration.
- `parameters`: The parameters that will be used while   browsing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/networkbrowser/init(for:using:))*