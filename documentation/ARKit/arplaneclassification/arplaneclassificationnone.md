# ARPlaneClassificationNone

**Framework**: ARKit  
**Kind**: case  
**Role**: Enumeration Case

No classification is available for the plane anchor.

**Availability**:
- iOS
- iPadOS

## Declaration

```c
ARPlaneClassificationNone
```

## Discussion

When a plane anchor has no classification, the [`classificationStatus`](../arplaneanchor/classificationstatus.md) property indicates the reason: the classification process might be unavailable or incomplete, or ARKit may not have been able to conclusively identify the plane.

## See Also

### Plane Classifications
- [ARPlaneClassificationWall](./arplaneclassificationwall.md)
  The plane anchor represents a real-world wall or similar large vertical surface.
- [ARPlaneClassificationFloor](./arplaneclassificationfloor.md)
  The plane anchor represents a real-world floor, ground plane, or similar large horizontal surface.
- [ARPlaneClassificationCeiling](./arplaneclassificationceiling.md)
  The plane anchor represents a real-world ceiling or similar overhead horizontal surface.
- [ARPlaneClassificationTable](./arplaneclassificationtable.md)
  The plane anchor represents a real-world table, desk, bar, or similar flat surface.
- [ARPlaneClassificationSeat](./arplaneclassificationseat.md)
  The plane anchor represents a real-world chair, stool, bench or similar flat surface.
- [ARPlaneClassificationDoor](./arplaneclassificationdoor.md)
  The plane anchor represents a real-world door, or similar archway.
- [ARPlaneClassificationWindow](./arplaneclassificationwindow.md)
  The plane anchor fits the description of a real-world window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneclassification/arplaneclassificationnone)*