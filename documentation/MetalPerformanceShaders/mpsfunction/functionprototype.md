# functionPrototype()

**Framework**: Metal Performance Shaders  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func functionPrototype() -> String
```

#### Discussion

Get a source level representation of the function prototype

If your application is building its shaders from source at run time, this string will declare the appropriate function prototypes for the conversion routine appropriate to the version of MetalHDR you are currently running.

```None
         Note: It is expected that most applications will not use this interface because they
         are building kernels offline from a .metallib. Such applications should simply:

            #include <MPSFunctions/MPSFunctions.h>

         in their .metal file, and declare any functions produced by this object using

            MPSFUNCTION_DECLARE_COLOR_CONVERSION( _functionName );

         or similar, depending on the type of the function created. The _functionName should
         match the name passed to the object -init method.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsfunction/functionprototype())*