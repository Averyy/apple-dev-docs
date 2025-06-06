# Create or Replace a Thumbnail

**Framework**: ClassKit Catalog API  
**Kind**: httpRequest

Store an image that represents one of your app’s assignable activities.

**Availability**:
- ClassKit 1.0+

#### Discussion

You can associate a thumbnail image with one or more contexts. Create an association by matching the `thumbnailId` value that you provide as a query parameter to this call with the `thumbnailId` field of a [`Context.Data`](context/data-data.dictionary.md) object that you upload with a call to [`Create or Replace Contexts`](create-or-replace-contexts.md). Upload the context that references a thumbnail before uploading the thumbnail.

Provide the thumbnail image as binary data in the request body. For example, after obtaining a web token, as [`Authenticating Calls to the ClassKit Catalog API`](authenticating-calls-to-the-classkit-catalog-api.md) describes, you could use the following `curl` command to upload the image in the file `catalog.png`:

```shell
% curl --request POST \
       --url 'https://classkit-catalog.apple.com/v1/thumbnails?thumbnailId=catalog.png&environment=production' \
       --header 'authorization: Bearer <JWT>' \
       --header 'content-type: image/png' \
       --data-binary '@catalog.png'
```

Follow the same guidelines for creating thumbnails as you follow when working with the ClassKit API in your app. In particular, provide images that are at least 80 x 80 pixels, and no larger than 330 x 330 pixels. The system ignores thumbnails that are too small, and scales down thumbnails that are too large. Use a thumbnail with the maximum dimensions to produce the best result across devices.

If you delete every context that references a thumbnail, the system automatically deletes the thumbnail image as well.

## See Also

- [Get a Thumbnail](get-a-thumbnail.md)
  Fetch the image for one of your app’s assignable activities.
- [Delete a Thumbnail](delete-a-thumbnail.md)
  Remove one of the images for your app’s assignable activities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/classkitcatalogapi/create-or-replace-a-thumbnail)*