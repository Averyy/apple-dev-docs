# Deprecated symbols

**Framework**: AVFoundation  
**Role**: API Collection

Review unsupported symbols and their replacements.

## Overview

See [Loading media data asynchronously](./loading-media-data-asynchronously.md) for information on the replacement API that’s based on Swift’s concurrency features.

## Topics

### Loading property values
- [func loadValuesAsynchronously(forKeys: [String], completionHandler: (() -> Void)?)](./avasynchronouskeyvalueloading/loadvaluesasynchronously%28forkeys,completionhandler%29.md)
  Tells the asset to load the values of all of the specified keys that aren’t already loaded.
- [func statusOfValue(forKey: String, error: NSErrorPointer) -> AVKeyValueStatus](./avasynchronouskeyvalueloading/statusofvalue%28forkey,error%29.md)
  Returns a status that indicates whether a property value is immediately available without blocking the calling thread.
- [enum AVKeyValueStatus](./avkeyvaluestatus.md)
  Values that indicate the loaded status of a property.

## See Also

### Deprecated
- [func loadValuesAsynchronously(forKeys: [String], completionHandler: (() -> Void)?)](./avasynchronouskeyvalueloading/loadvaluesasynchronously%28forkeys,completionhandler%29.md)
  Tells the asset to load the values of all of the specified keys that aren’t already loaded.
- [func statusOfValue(forKey: String, error: NSErrorPointer) -> AVKeyValueStatus](./avasynchronouskeyvalueloading/statusofvalue%28forkey,error%29.md)
  Returns a status that indicates whether a property value is immediately available without blocking the calling thread.
- [enum AVKeyValueStatus](./avkeyvaluestatus.md)
  Values that indicate the loaded status of a property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasynchronouskeyvalueloading-deprecated-symbols)*