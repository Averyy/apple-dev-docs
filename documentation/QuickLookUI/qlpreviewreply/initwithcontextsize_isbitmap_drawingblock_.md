# initWithContextSize:isBitmap:drawingBlock:

**Framework**: Quick Look UI  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- macOS 12.0+

## Declaration

```objc
- (instancetype) initWithContextSize:(CGSize) contextSize isBitmap:(BOOL) isBitmap drawingBlock:(BOOL (^)(CGContextRef context, QLPreviewReply *reply, NSError **error)) drawingBlock;
```

## Discussion

Use this method to provide a preview by drawing into a context.

## Parameters

- `contextSize`: The size of your image.
- `isBitmap`: Whether the context should be bitmap or vector.
- `drawingBlock`: The preview should be drawn into the context passed to this block. The QLPreviewReply passed into this block is the same as the one created by this method and is provided for convenience for any further updates to its properties during the drawing block. Return YES if the preview was successfully drawn into the context. Return NO and populate error otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewreply/initwithcontextsize:isbitmap:drawingblock:)*