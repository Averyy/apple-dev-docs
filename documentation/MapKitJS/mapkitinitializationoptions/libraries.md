# libraries

**Framework**: MapKit JS  
**Kind**: property

An array of libraries to load at initialization.

**Availability**:
- MapKit JS 5.75+

## Declaration

```swift
libraries?: string[];
```

#### Discussion

> **Note**:  The full bundle of MapKit JS ignores this option.

MapKit JS divides its interfaces into libraries that you can specify when loading the framework. To optimize your app load time, pick only the interfaces you need:

You can set the libraries to load statically by defining them within script tag in the `data-libraries` attribute or in the [`load(libraryNames)`](mapkit/load.md) method, or by passing a `libraries` property in the [`init(options)`](mapkit/init.md) options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkitinitializationoptions/libraries)*