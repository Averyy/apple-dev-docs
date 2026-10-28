# Testing FxPlug plug-ins

**Framework**: Professional-Video-Applications  
**Role**: Article

Test and debug FxPlug plug-ins using a variety of methods.

## Overview

A number of subtle rendering situations can arise during the normal use of your plug-in, and your users expect your plug-in to handle them all correctly. You can test for most rendering issues by creating a single project that tests your plug-in for a variety of common scenarios, including:

- Previewing timeline and layer lists
- Displaying at proxy resolution
- Rendering at a lower resolution
- Handling non-square pixels and fields

> **Note**:  The test projects described in this article outline how to test a filter. To test a generator, simply use your own generator instead of the Checkerboard generator, and disregard applying a filter. To ensure correct results, use pixel transforms on the input and output image; see [Optimizing FxPlug plug-ins](./optimizing-fxplug-plug-ins.md). To test for correctness, check the results of your generator.

### Set up a test project

1. In Motion, create a new project with the following custom settings: Resolution: 1920 x 1080 pixels; Field Order: None; Aspect Ratio: Square (1.0); Frame Rate: 30 fps; Duration: 10 seconds.
2. Add three layers to your project—each containing the same generator. Click the Library tab, select the Generators category, and highlight the built-in Checkerboard generator. (If you prefer, you can test using your own FxGenerator generator instead of the built-in Checkerboard generator). Click Apply three times to add three copies of the generator to the canvas. (If you’re testing with your own generator, use that plug-in instead of the Checkerboard generator). You should now have an HD project with square pixels and three generators in the timeline.
3. Set the pixel aspect ratio for the bottom generator. In the layer list, highlight the last generator in the list, click the Inspector tab, and then click the Generator tab to see the controls. The first three parameters of every generator are width, height, and pixel aspect ratio. For the bottom generator, set the width to 1440 pixels and, from the Pixel Aspect Ratio pop-up menu, select HD (960x720, 1440x1080).
4. Set the pixel aspect ratio for the middle generator. Highlight the middle generator in the layer list, and change its width to 960 pixels and its pixel aspect ratio to Anamorphic 2:1. This changes the generator to have a pixel aspect ratio of 2, which should highlight any problems your plug-ins have with non-square pixels.
5. Keep the third and final layer’s settings as they are.

### Test for pixel aspect ratio correctness

Test your plug-in filter by applying it to each generator in each layer of the project. As you deactivate the top layer, the middle layer should look the same. Likewise, as you deactivate the middle layer, the bottom layer should look the same. If you find that isn’t the case, you aren’t handling non-square pixels correctly. The simplest way to do so is to use the input and output image’s pixel transforms.

Start by applying the same filter to each generator in your project and then turn off the top layer. The middle layer should look the same as the top layer did. This technique of toggling layer visibility is a useful way to do A/B testing, where you’re interested in seeing if something is different. The following illustration shows the expected output of the checkerboard generator.

![Image showing a checkerboard pattern with square shapes.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3586108@2x.png)

Now turn off the middle layer. The bottom layer should look the same as the middle and top layers. All layers should look like the checkerboard in the image above, regardless of the generator’s pixel aspect ratio setting.

If any of your layers are squeezed or stretched out, as shown in the following illustration, then your plug-in isn’t handling non-square pixels correctly.

![Image showing checkerboard pattern in Motion with stretched shapes that are no longer square.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3586106@2x.png)

### Test the correctness of your point parameters

Another important test for your plug-in is to make sure that your point parameters are creating their effects in the correct place, and that any parameters using absolute pixels create the same look, regardless of the pixel aspect ratio.

1. In the top layer in the checkerboard generator, adjust the Size parameter. Set the size of each checker in absolute pixels.
2. Make the same adjustment to the Size parameter for the middle and bottom layers. Although the second layer (anamorphic) has half as many pixels across as the layer with a pixel aspect ratio of 1, the checkers should remain the same size in both layers for any given value of the parameter.

### Test for proxy resolution correctness

Proxy resolution uses uniform scaling, while pixel aspect ratio uses non-uniform scaling. If you’re using pixel transforms to do your scaling and the results of your tests for pixel aspect ratio correctness are good, then testing your proxy resolution should be a simple matter.

1. In Motion, click Render and select Half as the new resolution. The resolution of the footage drops, but your effect dimensions shouldn’t change.
2. Click Render again and select Quarter to switch to quarter resolution. If your effect dimensions remain the same, then your plug-in is properly handling proxy resolution.

The following figure shows the checkerboard generator at full resolution.

![Image showing render resolution set to Full in Motion.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3586104@2x.png)

The following figure shows the checkerboard generator at half resolution, but incorrectly rendering the effect.

![Image showing render resolution set to Half in Motion, but the squares in the checkerboard pattern are incorrectly scaled.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3586107@2x.png)

The following figure shows the checkerboard generator at half resolution, and correctly rendering the effect.

![Image showing render resolution set to Half in Motion, with the squares in the checkerboard pattern correctly scaled.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3586105@2x.png)

### Testing for correct thumbnail previews

If you have pixel aspect ratio and proxy resolution working correctly, your plug-in is probably handling thumbnail generation properly. Check by opening the layer list and examining the previews. If the previews show any enlargement or cropping, then your plug-in isn’t handling thumbnail generation correctly.

This next example is rendered incorrectly. Notice that the preview in the layer list shows checkers that are the same size as the checkers in the canvas, which is at full-resolution.

![Image showing the thumbnail rendered incorrectly.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3586109@2x.png)

The preview should show a smaller version of the entire layer in the layer list, as shown here:

![Image showing the thumbnail rendered correctly.](https://developer.apple.com/tutorials/images/com.apple.professionalvideoapplications/media-3586103@2x.png)

### Troubleshoot rendering problems

Any number of things can go wrong when dealing with non-square pixels and proxy resolution. The most common problem is that some aspect of your effect grows or shrinks inappropriately when applied to non-uniformly scaled footage. Circles get stretched or compressed into ovals, or things are twice as large as they should be.

Transform the coordinates of each pixel from the output image’s pixel space into full-sized, square-pixel image coordinates, using the inverse pixel transform. Then perform your computations on those coordinates as you would normally—without scaling them. Finally, transform the computed coordinates back into the input image’s pixel space using the pixel transform to sample the input image. See [Optimizing FxPlug plug-ins](./optimizing-fxplug-plug-ins.md) for more information on pixel transforms.

### Debug your plug-in

To test your plug-in code in a target application, choose Project > Scheme > Edit Scheme in your Xcode project window, and then, below the Info tab for the Run action, choose Motion or Final Cut Pro as the executable.

To see all messages that the plug-in generates, launch Console, and search for the process name of your plug-in.

If you want to test your plug-in further on whether it can handle the quitting or restarting of its process, try force quitting its process through Activity Monitor or using the command `kill -9` followed by the process ID of your plugin, which you can find in Activity Monitor. You can also write a shell script to perform a repeatable, automated test. An example of a script is listed below.

```other
#!/bin/sh
PID=0  #enter process ID here  
SLEEPSECONDS=10  #sleep time between force quitting
while [ 1 -ne 0 ]
do
    if [[ -n $PID ]]
    then
        echo "Force quitting process with ID: $PID"
        kill -9 $PID
    else
        echo "No process found."
    fi
    echo "Sleeping for $SLEEPSECONDS seconds…"
    sleep $SLEEPSECONDS
done
```

Run your script in Terminal by first using `chmod +x yourscript.sh` to execute permissions and then `./yourscript.sh` to run it.

> ⚠️ **Warning**:  Force quitting your plug-in more than twice in a span of 30 seconds may cause the host to consider it unresponsive.

## See Also

### Testing and deployment
- [Preparing plug-ins for use in Final Cut Pro](./preparing-plug-ins-for-use-in-final-cut-pro.md)
  Add a plug-in to a Motion effect template to use in Final Cut Pro.
- [Notarizing your FxPlug plug-in](./notarizing-your-fxplug-plug-in.md)
  Give users confidence in your FxPlug plug-in by enabling notarization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional-video-applications/testing-fxplug-plug-ins)*