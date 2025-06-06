# render(atTime:arguments:)

**Framework**: Quartz  
**Kind**: method

Overrides to perform  your custom operations prior to or after rendering a frame of a composition.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
func render(atTime time: TimeInterval, arguments: [AnyHashable : Any]!) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/swift/false) if your custom rendering fails, otherwise, [`true`](https://developer.apple.com/documentation/swift/true).

#### Discussion

Do not call this method directly. You override this method only for subclasses of the `QCView` class and only if you want to perform custom operations or OpenGL rendering before and/or after  Quartz Composer renders a frame of the composition.

The most common reasons to override this method are to:

- synchronize communication with the composition. For example, you might want to set input parameters of the composition. By overriding this method, you can set parameters only when necessary and only at a specific time.
- underlay or overlay custom OpenGL rendering.

To synchronize communication between a composition and another part of the application, the implementation looks similar to the following:

```objc
 
- (BOOL) renderAtTime:(NSTimeInterval)time
            arguments:(NSDictionary*)arguments
{
  // Your code to computer the value of myParameterValue
  [self setValue:myParameterValue forInputKey:@"myInput"];
 
  BOOL success = [super renderAtTime:time arguments:arguments];
 
  id result = [self valueForOutputKey:@"myOutput"];
  //Your code to perform some operation on the result
 
  return success;
}
 
```

To perform OpenGL drawing in a `QCView` object, follow these guidelines:

- Use the OpenGL context of the `QCView` object to do drawing. You can retrieve the OpenGL context by calling `[self openGLContext]`. Note that this context won’t  necessarily be set as the current OpenGL context.
- Use CGL macros instead of managing the current OpenGL context yourself.

OpenGL performs a global context and renderer lookup for each command it executes to ensure that all OpenGL commands are issued to the correct rendering context and renderer. There is significant overhead associated with these lookups that can measurably affect  performance. CGL macros let you provide a local context variable and cache the current renderer in that variable. They are simple to use, taking only a few lines of code to set up.

- Save and restore all state changes except the ones that are part of `GL_CURRENT_BIT` (RGBA color, color index, normal vector, texture coordinates, and so forth).
- Check for OpenGL errors with `glGetError`.

Here’s an example implementation of this method using OpenGL to draw an overlay:

```objc
#import <OpenGL/CGLMacro.h>  // Set up using macros
 
- (BOOL) renderAtTime:(NSTimeInterval)time
            arguments:(NSDictionary*)arguments
{
    BOOL success = [super renderAtTime:time arguments:arguments];
 
    // Use the OpenGL context of the view for drawing.
    CGLContextObj cgl_ctx = [[self openGLContext] CGLContextObj];
 
    // Save and set OpenGL states appropriately.
    glGetIntegerv(GL_MATRIX_MODE, &saveMode);
    glMatrixMode(GL_MODELVIEW);
    glPushMatrix();
    glRotatef(45.0, 0.0, 0.0, 1.0);
 
    // The code that performs OpenGL drawing goes here.
    //After drawing, restore original OpenGL states.
    glPopMatrix();
    glMatrixMode(saveMode);
 
    // Check for errors.
    glGetError();
    return success;
}
 
```

## Parameters

- `time`: The rendering time, in seconds, of the composition frame.
- `arguments`: An optional dictionary that can contain   or   and the associated values. (See   or more information.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcview/render(attime:arguments:))*