# load(_:allowExecutableCode:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Loads filters from an image unit that have the appropriate executable status.

**Availability**:
- macOS 10.7+ - Deprecated in 10.15

## Declaration

```swift
class func load(_ url: URL!, allowExecutableCode: Bool)
```

```objc
+ (void) loadPlugIn:(NSURL *) url allowExecutableCode:(BOOL) allowExecutableCode;
```

#### Discussion

You need to call this method only once to load a specific image unit. The behavior of this method is not defined for multiple calls for the same image unit. If you pass `false` for the `allowExecutableCode` parameter, Core Image will load only pure kernel filters that run entirely on the GPU, ignoring filters implemented using compiled Objective-C code.

## Parameters

- `url`: The location of the image unit to load.
- `allowExecutableCode`: `true` to load all filters from the image unit, or `false` to load only those filters without CPU executable code.

## See Also

### Deprecated
- [class func loadAllPlugIns()](./loadallplugins%28%29.md)
  Scans directories for files that have the `.plugin` extension and then loads the image units.
- [+ loadPlugIn:allowNonExecutable:](./loadplugin_allownonexecutable_.md)
  Loads filters from an image unit that have the appropriate executable status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciplugin/load(_:allowexecutablecode:))*