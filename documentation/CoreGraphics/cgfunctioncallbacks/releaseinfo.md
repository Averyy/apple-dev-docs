# releaseInfo

**Framework**: Core Graphics  
**Kind**: property

If non-`NULL`,the callback used to release the `info` parameterpassed to [`init(info:domainDimension:domain:rangeDimension:range:callbacks:)`](cgfunction/init(info:domaindimension:domain:rangedimension:range:callbacks:).md).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var releaseInfo: CGFunctionReleaseInfoCallback?
```

## See Also

- [var evaluate: CGFunctionEvaluateCallback?](cgfunctioncallbacks/evaluate.md)
  The callback that evaluates the function.
- [var version: UInt32](cgfunctioncallbacks/version.md)
  The structure version number. For this structure,the version should be `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfunctioncallbacks/releaseinfo)*