# isSynchronous

**Framework**: Photos  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether Photos processes the image request synchronously.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isSynchronous: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isSynchronous) BOOL synchronous;
```

## Discussion

If `false` (the default), the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](../phimagemanager/requestimage%28for,targetsize,contentmode,options,resulthandler%29.md) method returns immediately. Depending on the [`deliveryMode`](./deliverymode.md) property, Photos may call your `resultHandler` block before the method returns, at some later time, or both.

If `true`, the [`requestImage(for:targetSize:contentMode:options:resultHandler:)`](../phimagemanager/requestimage%28for,targetsize,contentmode,options,resulthandler%29.md) method blocks the calling thread until image data is ready or an error occurs. Photos calls your result handler block exactly once.

> **Note**:  Perform synchronous requests from a background thread only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phimagerequestoptions/issynchronous)*