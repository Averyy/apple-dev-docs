# LIVEPHOTOSKIT_LOADED

**Framework**: LivePhotosKit JS  
**Kind**: var

An event that is fired when LivePhotosKit JS is loaded.

**Availability**:
- LivePhotosKit JS 1.0+

## Declaration

```swift
const String LIVEPHOTOSKIT_LOADED;
```

#### Discussion

This event is fired when `livephotoskit.js` is loaded asynchronously. It always has the value `livephotoskitloaded`.

For example, log this event as follows.

```javascript
document.addEventListener('livephotoskitloaded', function(e) {
  console.log('Loaded LivePhotosKit JS');
});
```

## See Also

- [VERSION](livephotoskit/version.md)
  The version of LivePhotosKit JS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/livephotoskitjs/livephotoskit/livephotoskit_loaded)*