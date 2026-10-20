# init(data:)

**Framework**: Core MIDI  
**Kind**: init  
**Role**: Initializer

Creates a MIDI profile for the specified data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(data: Data)
```

```objc
- (instancetype) initWithData:(NSData *) data;
```

## Parameters

- `data`: The profile’s unique byte sequence.

## See Also

### Creating a Profile
- [init(data: Data, name: String)](./init%28data,name%29.md)
  Creates a named MIDI profile for the specified data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiciprofile/init(data:))*