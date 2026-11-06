# FoveatedStreamingSession.ConfigurationValue

**Framework**: Foveated Streaming  
**Kind**: enum  
**Role**: Enumeration

A value in the configuration passed to a streaming provider.

**Availability**:
- visionOS 27.3+ (Beta)

## Declaration

```swift
enum ConfigurationValue
```

## Overview

Streaming providers often accept connection parameters specific to their streaming protocol, such as a video bitrate or codec selection. Supply those parameters as a `[String: ConfigurationValue]` dictionary when you call [`connect(endpoint:streamingProvider:configuration:)`](./connect%28endpoint,streamingprovider,configuration%29.md):

```swift
try await session.connect(
    endpoint: .local(ipAddress: address, port: port),
    streamingProvider: provider,
    configuration: [
        "com.example.MyProvider.maxBitrate": .int(50_000_000),
        "com.example.MyProvider.lowLatencyMode": .bool(true)
    ]
)
```

## Topics

### Enumeration Cases
- [case array([FoveatedStreamingSession.ConfigurationValue])](./configurationvalue/array%28_%29.md)
  An ordered list of values.
- [FoveatedStreamingSession.ConfigurationValue.bool(_:)](./configurationvalue/bool%28_%29.md)
  A Boolean value.
- [FoveatedStreamingSession.ConfigurationValue.data(_:)](./configurationvalue/data%28_%29.md)
  A raw data value.
- [case dictionary([String : FoveatedStreamingSession.ConfigurationValue])](./configurationvalue/dictionary%28_%29.md)
  A nested dictionary of values, keyed by name.
- [FoveatedStreamingSession.ConfigurationValue.double(_:)](./configurationvalue/double%28_%29.md)
  A double-precision floating-point value.
- [FoveatedStreamingSession.ConfigurationValue.float(_:)](./configurationvalue/float%28_%29.md)
  A single-precision floating-point value.
- [FoveatedStreamingSession.ConfigurationValue.int(_:)](./configurationvalue/int%28_%29.md)
  An integer value.
- [FoveatedStreamingSession.ConfigurationValue.simdDouble2(_:)](./configurationvalue/simddouble2%28_%29.md)
  A two-component vector of double-precision values.
- [FoveatedStreamingSession.ConfigurationValue.simdDouble3(_:)](./configurationvalue/simddouble3%28_%29.md)
  A three-component vector of double-precision values.
- [FoveatedStreamingSession.ConfigurationValue.simdDouble4(_:)](./configurationvalue/simddouble4%28_%29.md)
  A four-component vector of double-precision values.
- [FoveatedStreamingSession.ConfigurationValue.simdFloat2(_:)](./configurationvalue/simdfloat2%28_%29.md)
  A two-component vector of single-precision values.
- [FoveatedStreamingSession.ConfigurationValue.simdFloat3(_:)](./configurationvalue/simdfloat3%28_%29.md)
  A three-component vector of single-precision values.
- [FoveatedStreamingSession.ConfigurationValue.simdFloat4(_:)](./configurationvalue/simdfloat4%28_%29.md)
  A four-component vector of single-precision values.
- [FoveatedStreamingSession.ConfigurationValue.string(_:)](./configurationvalue/string%28_%29.md)
  A string value.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foveatedstreaming/foveatedstreamingsession/configurationvalue)*