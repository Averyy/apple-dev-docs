# language

**Framework**: MapKit JS  
**Kind**: property

A language ID that determines the language to use for displaying addresses.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get language(): string | null;
set language(value: string | null);
```

#### Discussion

When you set the [`language`](service/language.md) property to a language ID (such as `fr-CA` or `en-GB`), the service returns results in this language, if available. If [`language`](service/language.md) isn’t set when initializing a [`Service`](service.md) object, then the service uses the language you provided when you initialized MapKit.

The default value is `null`. The language can be unset by setting [`language`](service/language.md) to `null` or `undefined`.

## See Also

- [new Geocoder(options)](geocoder/geocoderconstructor.md)
  Creates a geocoder object and sets optional language and user location properties.
- [interface ServiceConstructorOptions](serviceconstructoroptions.md)
  Common options you provide when you create a service object.
- [getsUserLocation](service/getsuserlocation.md)
  A Boolean value that indicates whether the request returns results near a person’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/service/language)*