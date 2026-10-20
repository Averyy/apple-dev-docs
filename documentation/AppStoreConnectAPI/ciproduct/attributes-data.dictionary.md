# CiProduct.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The attributes that describe a Products resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiProduct.Attributes
```

## Properties

- `createdDate` (date-time): The date when you created the Xcode Cloud product.
- `name` (string): The name of the Xcode Cloud product.
- `productType` (string): A string that indicates whether the Xcode Cloud product is a framework or an app.

  **Allowed Values**: `APP`, `FRAMEWORK`

## See Also

### Objects
- [object CiProduct.Relationships](./relationships-data.dictionary.md)
  The relationships of the Products resource you included in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciproduct/attributes-data.dictionary)*