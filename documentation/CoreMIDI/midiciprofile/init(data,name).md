# init(data:name:)

**Framework**: Core MIDI  
**Kind**: init  
**Role**: Initializer

Creates a named MIDI profile for the specified data.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(data: Data, name inName: String)
```

```objc
- (instancetype) initWithData:(NSData *) data name:(NSString *) inName;
```

## Parameters

- `data`: The profile’s unique byte sequence.
- `inName`: The profile name.

## See Also

### Creating a Profile
- [init(data: Data)](./init%28data%29.md)
  Creates a MIDI profile for the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofile/init(data:name:))*