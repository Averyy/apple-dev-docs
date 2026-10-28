# init(options:)

**Framework**: Media Library  
**Kind**: init  
**Role**: Initializer

Initializes the media library based on the specified load options.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.9+ - Deprecated in 10.15

> **Deprecated**: MediaLibrary.framework will be removed in a future OS version. Use Photos.framework or iTunesLibrary.framework instead.

## Declaration

```swift
init(options: [String : Any] = [:])
```

```objc
- (instancetype) initWithOptions:(NSDictionary<NSString *,id> *) options;
```

## Return Value

A new media library.

## Discussion

For descriptions of possible load options, see [Load Options Keys](../load-options-keys.md).

## Parameters

- `options`: A dictionary of load options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/medialibrary/mlmedialibrary/init(options:))*